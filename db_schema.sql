DROP TABLE IF EXISTS ITEMS;
DROP TABLE IF EXISTS TYPES;
DROP TABLE IF EXISTS ITEMS_TYPES;

CREATE TABLE ITEMS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    price REAL NOT NULL DEFAULT 0
);

CREATE TABLE TYPES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);

CREATE TABLE ITEMS_TYPES (
    item_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    FOREIGN KEY (item_id) REFERENCES ITEMS(id),
    FOREIGN KEY (type_id) REFERENCES TYPES(id)
);