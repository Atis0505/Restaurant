from enum import Enum


class InitSqlCommands(Enum):
    CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS User(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserName TEXT NOT NULL,
    Password TEXT NOT NULL,
    UNIQUE(UserName));"""
    CREATE_FOOD_CATEGORIES_TABLE = """
    CREATE TABLE IF NOT EXISTS FoodCategory(
    FoodCategoryID INTEGER PRIMARY KEY,
    FoodCategoryName TEXT NOT NULL,
    Description TEXT,
    Discount INTEGER);"""
    CREATE_FOOD_TABLE = """
    CREATE TABLE IF NOT EXISTS FoodItem(
    FoodItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    FoodName TEXT NOT NULL,
    Description TEXT,
    UnitPrice INTEGER NOT NULL,
    FoodCategory INTEGER,
    Discount INTEGER,
    FOREIGN KEY(FoodCategory) REFERENCES FoodCategory(FoodCategoryID));"""
    CREATE_DRINK_CATEGORIES_TABLE = """
    CREATE TABLE IF NOT EXISTS DrinkCategory(
    DrinkCategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    DrinkCategoryName TEXT NOT NULL,
    Description TEXT,
    AlcoholContent INTEGER,
    Discount INT);"""
    CREATE_DRINK_TABLE = """
    CREATE TABLE IF NOT EXISTS DrinkItem(
    DrinkItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    DrinkItemName TEXT NOT NULL,
    Description TEXT,
    UnitPrice INTEGER,
    DrinkCategory INTEGER,
    Discount INTEGER,
    FOREIGN KEY(DrinkCategory) REFERENCES DrinkCategory(DrinkCategoryID));"""
    CREATE_WORKER_TABLE = """
    CREATE TABLE IF NOT EXISTS Worker(
    WorkerID INTEGER PRIMARY KEY AUTOINCREMENT,
    WorkerName TEXT NOT NULL,
    WorkingHours INTEGER,
    StartDate NUMERIC,
    EndDate NUMERIC);"""
    CREATE_ORDER_TABLE = """
    CREATE TABLE IF NOT EXISTS RestaurantOrder(
    RestaurantOrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderName TEXT NOT NULL,
    TimeStamp NUMERIC,
    WorkerID INTEGER NOT NULL,
    Price INT,
    Paid NUMERIC,
    FOREIGN KEY(WorkerID) REFERENCES Worker(WorkerID));"""
    CREATE_RESERVATIONS_TABLE = """
    CREATE TABLE IF NOT EXISTS Reservation(
    ReservationID INTEGER PRIMARY KEY AUTOINCREMENT,
    ReservationName TEXT NOT NULL,
    PeopleNumber INTEGER,
    TimeFrom NUMERIC,
    TimeTo NUMERIC,
    Price INTEGER);"""


class DefaultDatabaseStructure:
    CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS User(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserName TEXT NOT NULL,
    Password TEXT NOT NULL,
    UNIQUE(UserName));"""
    CREATE_FOODITEM_CATEGORY_TABLE = """
    CREATE TABLE IF NOT EXISTS FoodCategory(
    FoodCategoryID INTEGER PRIMARY KEY,
    FoodCategoryName TEXT NOT NULL,
    Description TEXT,
    Discount INTEGER);"""
    CREATE_DRINKITEM_CATEGORY_TABLE = """
    CREATE TABLE IF NOT EXISTS DrinkCategory(
    DrinkCategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    DrinkCategoryName TEXT NOT NULL,
    Description TEXT,
    AlcoholContent INTEGER,
    Discount INT);"""
    CREATE_ORDER_ITEM_TABLE = """"""
    CREATE_FOODITEM_TABLE = """"""
    CREATE_DRINKITEM_TABLE = """"""
    CREATE_WORKER_TABLE = """"""
    CREATE_PLACED_ORDER_TABLE = """"""
