{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "print(\"-------- START OF ETL --------\")\n",
    "\n",
    "# Initiate a New SQLite DB\n",
    "\n",
    "# To Create an Empty SQLlite DB:\n",
    "# Simply sqlite3.connect() to Whatever you \n",
    "# want your new DB to be called.\n",
    "\n",
    "# sqlite3.connect('Type your New DataBase name here.db')\n",
    "\n",
    "db_path = 'vrb_know.sqlite3'\n",
    "\n",
    "# Establish Connection\n",
    "conn = sqlite3.connect(db_path)\n",
    "print(\"SQLite Connection Established\")\n",
    "# Intantiate Cursor\n",
    "curs = conn.cursor()\n",
    "print(\"Cursor Instantiated\")\n",
    "\n",
    "\n",
    "Q_CREATE_TABLE_STUDENTS = \"\"\" \n",
    "    CREATE TABLE IF NOT EXISTS market_summary (\n",
    "        student VARCHAR(50),\n",
    "        studied TEXT,\n",
    "        grade INT,\n",
    "        age INT,\n",
    "        sex VARCHAR(10)\n",
    "    );\n",
    "    \"\"\"\n",
    "\n",
    "# Excecute CREATE TABLE Query\n",
    "curs.execute(Q_CREATE_TABLE_STUDENTS)\n",
    "\n",
    "# Commit New Table on the Connection\n",
    "conn.commit()\n",
    "print(\"Table Successfully Created\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "vrb-know",
   "language": "python",
   "name": "vrb-know"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
