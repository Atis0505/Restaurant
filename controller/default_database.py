from enum import Enum


class InitSqlCommands(Enum):
    CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS Users(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserName TEXT NOT NULL,
    Password TEXT NOT NULL,
    UNIQUE(UserName));"""
    CREATE_FOOD_CATEGORIES_TABLE = """
    CREATE TABLE IF NOT EXISTS FoodCategories(
    FoodCategoryID INTEGER PRIMARY KEY,
    FoodCategoryName varchar(20) NOT NULL,
    Discount INTEGER,
    PicturePath varchar(150));"""
    CREATE_FOOD_TABLE = """
    CREATE TABLE IF NOT EXISTS FoodItem(
    FoodItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    FoodName TEXT NOT NULL,
    Quantity INTEGER,
    UnitPrice INTEGER NOT NULL,
    FoodCategory INTEGER NOT NULL,
    Discount INTEGER,
    PicturePath varchar(150),
    FOREIGN KEY(FoodCategory) REFERENCES FoodCategories(FoodCategoryID));"""
    CREATE_DRINK_CATEGORIES_TABLE = """
    CREATE TABLE IF NOT EXISTS DrinkCategories(
    DrinkCategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    DrinkCategoryName TEXT NOT NULL,
    AlcoholContent NUMERIC,
    AlcoholDegree TEXT,
    Discount INT);"""
    CREATE_DRINK_TABLE = """
    CREATE TABLE IF NOT EXISTS DrinkItemID(
    DrinkItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    DrinkItemName TEXT NOT NULL,
    Quantity INTEGER,
    UnitPrice INTEGER,
    Size NUMERIC,
    Unit varhcar(20),
    DrinkCategory INTEGER NOT NULL,
    Discount INTEGER,
    PicturePath varchar(150),
    FOREIGN KEY(DrinkCategory) REFERENCES DrinkCategories(DrinkCategoryID));"""
    CREATE_WORKER_TABLE = """
    CREATE TABLE IF NOT EXISTS Workers(
    WorkerID INTEGER PRIMARY KEY AUTOINCREMENT,
    WorkerName TEXT NOT NULL,
    WorkingHours INTEGER,
    StartDate NUMERIC,
    EndDate NUMERIC);"""
    CREATE_ORDER_TABLE = """
    CREATE TABLE IF NOT EXISTS RestaurantOrder(
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderName TEXT NOT NULL,
    TimeStamp NUMERIC,
    WorkerID INTEGER NOT NULL,
    Price INT,
    Paid NUMERIC,
    FOREIGN KEY(WorkerID) REFERENCES Worker(WorkerID));"""
    CREATE_RESERVATIONS_TABLE = """
    CREATE TABLE IF NOT EXISTS Reservations(
    ReservationID INTEGER PRIMARY KEY AUTOINCREMENT,
    ReservationName TEXT NOT NULL,
    PeopleNumber INTEGER,
    TimeFrom NUMERIC,
    TimeTo NUMERIC,
    Price INTEGER);"""
