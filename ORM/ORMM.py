from os import getenv
from dotenv import load_dotenv
import psycopg2
load_dotenv()

class DB:
    connection = psycopg2.connect(
        dbname=getenv('DB_NAME'),
        user=getenv('DB_USER'),
        host=getenv('HOST'),
        port=getenv('PORT'),
        password=getenv('PASSWORD'),
    )
    cursor = connection.cursor()

    def insert(self):
        self_dict = self.__dict__
        del self_dict['param']
        table_name = self.__class__.__name__.lower() + "s"
        col_name = " , ".join(self_dict.keys())
        format = " , ".join(["%s"] * len(self_dict.values()))
        params = tuple(self_dict.values())
        query = f"insert into {table_name} ({col_name}) values ({format})"
        self.cursor.execute(query, params)
        self.connection.commit()

    def select(self, **conditions):
        self_dict = self.__dict__
        if 'id' in self_dict and self_dict.get('id') is None:
            del self_dict['id']

        condition = ""
        if conditions:
            condition = "where " + " = %s and ".join(conditions.keys()) + " = %s"

        if not self.param:
            field = "*"
        else:
            field = " , ".join(self.param)
        params = tuple(conditions.values())
        table_name = self.__class__.__name__.lower() + "s"
        query = f"select {field} from {table_name} {condition}"
        self.cursor.execute(query, params)
        column_names = [desc[0] for desc in self.cursor.description]
        result = [self.__class__(**dict(zip(column_names, row))) for row in self.cursor.fetchall()]
        return result

    def update(self, **conditions):
        table_name = self.__class__.__name__.lower()+"s"
        condition = ""
        if conditions:
            condition = "where " + " = %s and ".join(conditions.keys()) + " = %s"
        self_dict=self.__dict__
        set_values=",".join(f"{key}= %s" for key in self_dict.keys())
        params=tuple(self_dict.values())+tuple(conditions.values())
        query=f"update {table_name} set {set_values} {conditions} "
        self.cursor.execute(query, params)
        self.connection.commit()

    def delete(self, **conditions):
        condition = ""
        if conditions:
            condition = "where " + " = %s and ".join(conditions.keys()) + " = %s"
        table_name = self.__class__.__name__.lower()
        query = f"delete from {table_name} {condition}"
        params = tuple(conditions.values())
        self.cursor.execute(query, params)
        self.connection.commit()