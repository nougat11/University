package com.example.myapplication.activities;

import android.media.MediaPlayer;
import android.os.Bundle;

import com.example.myapplication.db.DBAccess;
import com.example.myapplication.fragments.ItemInfoFragment;
import com.example.myapplication.fragments.NumberPick;
import com.example.myapplication.models.Item;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.fragment.app.Fragment;

import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.NumberPicker;

import com.example.myapplication.R;

import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;

public class InfoActivity extends AppCompatActivity implements NumberPicker.OnValueChangeListener {
    final static String TAG = "ALIEXPRESS";
    public static int ITEM_ID = 1;
    public static int CATEGORY_ID = 1;
    private List<Item> itemsCategory = new ArrayList();
    ListIterator<Item> iterator;
    int indexOfCurrentItem;
    int numberFromPicker = 1;
    private Button prevButton;
    private Button nextButton;
    private Button addToBucketButton;
    Item itemFromDB;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.d(TAG, "InfoActivity: onCreate");
        super.onCreate(savedInstanceState);
        CATEGORY_ID = getIntent().getExtras().getInt("category_id");
        ITEM_ID = getIntent().getExtras().getInt("item_id");
        setContentView(R.layout.activity_info);
        prevButton = findViewById(R.id.btnPrevFragment);
        nextButton = findViewById(R.id.btnNextFragment);
        addToBucketButton = findViewById(R.id.btnAddToBucket);
        final MediaPlayer mediaPlayer = MediaPlayer.create(this, R.raw.bass_click);
        loadInfo();
        setItemsFromDB();
        Fragment fragmentWithArgs = new ItemInfoFragment();
        Bundle args = new Bundle();
        args.putByteArray("ARG_ITEM_IMAGE", itemFromDB.getImage());
        args.putString("ARG_ITEM_NAME", itemFromDB.getName());
        args.putInt("ARG_ITEM_PRICE", itemFromDB.getPrice());
        args.putString("ARG_ITEM_DESC", itemFromDB.getDescription());
        fragmentWithArgs.setArguments(args);

        getSupportFragmentManager().beginTransaction()
                .add(R.id.containerView, fragmentWithArgs, "fragment")
                .commit();

        prevButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d(TAG, "InfoActivity: prevbutton click");
                ItemInfoFragment fragment = (ItemInfoFragment) getSupportFragmentManager().findFragmentByTag("fragment");
                mediaPlayer.start();
                if (fragment != null){
                    if (iterator.hasPrevious()){
                        Item prevItem = iterator.previous();
                        ITEM_ID = prevItem.getId();
                        itemFromDB = prevItem; // test
                        fragment.updateValues(prevItem);
                    }
                    else
                    {
                        Snackbar.make(v, "No previous item", Snackbar.LENGTH_SHORT)
                                .setAction("Action", null).show();
                    }
            }
        }
        });
        nextButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Log.d(TAG, "InfoActivity: nextbutton click");
                ItemInfoFragment fragment = (ItemInfoFragment) getSupportFragmentManager().findFragmentByTag("fragment");
                mediaPlayer.start();
                if (fragment != null){
                    if (iterator.hasNext()){
                        Item nextItem = iterator.next();
                        ITEM_ID = nextItem.getId();
                        itemFromDB = nextItem; // test
                        fragment.updateValues(nextItem);
                    }
                    else
                    {
                        Snackbar.make(v, "No next item", Snackbar.LENGTH_SHORT)
                                .setAction("Action", null).show();
                    }
                }
            }
        });
        addToBucketButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Log.d(TAG, "ItemInfoActivity: button buy clicked");
                //Amount picker
                mediaPlayer.start();
                showNumberPicker(v);
                //some database function

            }
        });

    }
    @Override
    public void onValueChange(NumberPicker numberPicker, int i, int i1) {
        Log.d(TAG, "ItemInfoActivity: changing color of "+ itemFromDB.getName());
        numberFromPicker = numberPicker.getValue();
        DBAccess dbAccess = DBAccess.getInstance(getApplicationContext());
        dbAccess.open();
        dbAccess.putItemInBasket(itemFromDB, numberFromPicker);
        dbAccess.close();
    }
    public void showNumberPicker(View view){
        NumberPick newFragment = new NumberPick();
        newFragment.setValueChangeListener(this);
        newFragment.show(getSupportFragmentManager(), "time picker");
    }
    private void loadInfo() {

        DBAccess dbAccess = DBAccess.getInstance(getApplicationContext());
        dbAccess.open();
        itemFromDB = dbAccess.getItem(ITEM_ID);
        //changing it color
        dbAccess.itemWasViewedChangeColor(ITEM_ID);
        dbAccess.close();
        Log.d(TAG, "InfoActivity : items loaded successfully");
    }
    private void setItemsFromDB(){
        DBAccess dbAccess = DBAccess.getInstance(getApplicationContext());
        dbAccess.open();
        itemsCategory = dbAccess.getItems(CATEGORY_ID);

        for (Item item : itemsCategory) {
            if (item.getId() == itemFromDB.getId()){
                itemFromDB = item;
                break;
            }

        }
        indexOfCurrentItem = itemsCategory.indexOf(itemFromDB);
        //setting iterator on position of current element
        iterator = itemsCategory.listIterator(indexOfCurrentItem);
        dbAccess.close();
        Log.d(TAG, "ItemInfoActivity : itemsInCategory successfully");
    }
}