import mysql.connector
from mysql.connector import Error
from Pack import *

class DbContext:
    dataBase=''
    dataBaseUser=''
    dataBasePassword=''
    dataBaseServer=''
    isSuccessConnection=0
    conn=mysql.connector

    def __init__ (self):
        self.dataBase=''
        self.dataBaseUser=''
        self.dataBasePassword=''
        self.dataBaseServer=''

    def init (sefl):
        self.dataBase=dataBase

    def SetFileds(self,dataBase,dataBaseUser,dataBasePassword,dataBaseServer):
        self.dataBase=dataBase
        self.dataBaseUser=dataBaseUser
        self.dataBasePassword=dataBasePassword
        self.dataBaseServer=dataBaseServer
      
    def CreateConnect(self):
        try:
            self.conn=mysql.connector.connect(
            host=self.dataBaseServer,
            database=self.dataBase,
            user=self.dataBaseUser,
            password=self.dataBasePassword)
            if self.conn.is_connected: 
                self.isSuccessConnection=1
        except Error as e:
            self.isSuccessConnection=0
    
    def ExecuteIntoDb(self,sql):
        mycursor = self.conn.cursor()
        mycursor.execute(sql)
        self.conn.commit()
       
    def ShowRecords(self,sql):
        mycursor = self.conn.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

                