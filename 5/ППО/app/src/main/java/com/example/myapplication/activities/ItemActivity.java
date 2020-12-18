package com.example.myapplication.activities;

import android.app.Activity;
import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Bundle;

import com.example.myapplication.adapters.ItemsAdapter;
import com.example.myapplication.db.DBAccess;
import com.example.myapplication.models.Item;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;

import com.example.myapplication.R;

import java.util.ArrayList;
import java.util.List;

public class ItemActivity extends Activity {
    public static final String TAG="ALIEXPRESS";
    public static int CATEGORY_ID = 1;
    private static String CATEGORY_NAME = "Category";
    private List<Item> itemsCategory = new ArrayList();
    ListView itemsList;
    FloatingActionButton button;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.d(TAG, "ItemActivity: onCreate");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_item);
        itemsList = findViewById(R.id.itemList);
        button = findViewById(R.id.floating_action_button);
        CATEGORY_NAME = getIntent().getExtras().getString("category_name");
        CATEGORY_ID = getIntent().getExtras().getInt("category_id");
        setItemsFromDb();
        ItemsAdapter itemsAdapter = new ItemsAdapter(this, R.layout.list_item, itemsCategory);
        itemsList.setAdapter(itemsAdapter);
        AdapterView.OnItemClickListener itemClickListener = new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Item selectedItem = (Item) parent.getItemAtPosition(position);
                Log.d(TAG, "ItemActivity: itemclick listner: click: " + selectedItem.getName());
                Intent intent = new Intent(ItemActivity.this, InfoActivity.class);
                intent.putExtra("item_id", selectedItem.getId());
                intent.putExtra("category_id", CATEGORY_ID);
                startActivity(intent);

            }
        };
        itemsList.setOnItemClickListener(itemClickListener);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d(TAG, "ItemActivity: Button clicked");
                final MediaPlayer mediaPlayer = MediaPlayer.create(getApplicationContext(), R.raw.bass_click);
                mediaPlayer.start();
                Intent intent = new Intent(ItemActivity.this, BasketActivity.class);// MainActivity.this -> getApplicationContext()
                startActivity(intent);
            }
        });



    }
    private void setItemsFromDb(){
        Log.d(TAG, "ItemActivity: setItemsFromDb");
        DBAccess dbAccess = DBAccess.getInstance(getApplicationContext());
        dbAccess.open();
        itemsCategory = dbAccess.getItems(CATEGORY_ID);
        dbAccess.close();
    }
}