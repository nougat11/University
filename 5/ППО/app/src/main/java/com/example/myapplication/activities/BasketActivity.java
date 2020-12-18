package com.example.myapplication.activities;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;

import com.example.myapplication.R;
import com.example.myapplication.SwipeListener;
import com.example.myapplication.adapters.BasketAdapter;
import com.example.myapplication.db.DBAccess;
import com.example.myapplication.db.DBHelper;
import com.example.myapplication.models.Basket;

import java.util.ArrayList;
import java.util.List;

public class BasketActivity extends Activity {
    private static final String TAG = "Aliexpress";
    private List<Basket> itemsInBasket = new ArrayList();
    SwipeListener onSwipeTouchListener;
    ListView itemsList;
    DBHelper dbHelper;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.d(TAG, "BasketActivity: onCreate");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_basket);
        itemsList = findViewById(R.id.basketList);
        setItemsFromDB();
        BasketAdapter basketAdapter = new BasketAdapter(this, R.layout.list_basket, itemsInBasket);
        itemsList.setAdapter(basketAdapter);

        AdapterView.OnItemClickListener itemListener = new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View v, int position, long id) {

                Basket selectedItem= (Basket) parent.getItemAtPosition(position);
                Intent intent = new Intent(BasketActivity.this, InfoActivity.class);
                intent.putExtra("item_id", selectedItem.getId_item());
                startActivity(intent);
            }
        };
        itemsList.setOnItemClickListener(itemListener);

        dbHelper = new DBHelper(this);
    }
    private void setItemsFromDB(){
        Log.d(TAG, "BasketActivity: setting items from DB");
        DBAccess dbAccess = DBAccess.getInstance(getApplicationContext());
        dbAccess.open();
        itemsInBasket = dbAccess.getItemsFromBacket();
        dbAccess.close();
    }
}