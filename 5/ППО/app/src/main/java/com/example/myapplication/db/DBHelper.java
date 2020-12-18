package com.example.myapplication.db;

import android.content.Context;
import com.readystatesoftware.sqliteasset.SQLiteAssetHelper;
public class DBHelper extends SQLiteAssetHelper{
    private static final String Name = "Base.db";
    private Context context;
    private static final int SCHEMA = 1;
    public DBHelper (Context context){
        super(context, Name, null, SCHEMA);
    }
}
