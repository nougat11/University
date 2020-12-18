package com.example.myapplication;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Build;
import android.os.Bundle;

import com.example.myapplication.activities.BasketActivity;
import com.example.myapplication.activities.ItemActivity;
import com.example.myapplication.adapters.CategoryAdapter;
import com.example.myapplication.db.DBAccess;
import com.example.myapplication.db.DBHelper;
import com.example.myapplication.models.Category;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

import android.os.Handler;
import android.os.HandlerThread;
import android.provider.MediaStore;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    private static final String TAG = "Aliexprexx";
    MediaPlayer Player1;
    private List<Category> categories = new ArrayList();
    ListView category;
    private HandlerThread handlerThread;
    private Handler backgroundHandler;
    FloatingActionButton bucket_button;
    DBHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        dbHelper = new DBHelper(this);
        createNotificationChannel();
        Log.d(TAG, "OnCreate: MainActivity");
        setContentView(R.layout.activity_main);
        setPlayers();
        Player1.start();
        setCategories();
        NotificationCompat.Builder builder = new NotificationCompat.Builder(this, "asd")
                .setSmallIcon(R.drawable.ic_basket_add)
                .setContentTitle("Скидки")
                .setContentText("asddas")
                .setPriority(NotificationCompat.PRIORITY_DEFAULT);

        category = (ListView) findViewById(R.id.categoryListView);
        bucket_button = findViewById(R.id.floating_action_button);
        CategoryAdapter stateAdapter = new CategoryAdapter(this, R.layout.list_category, categories);
        category.setAdapter(stateAdapter);
        AdapterView.OnItemClickListener itemListener = new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Category selected = (Category) parent.getItemAtPosition(position);
                Log.d(TAG, "MainActivity: category selected");
                Intent intent = new Intent(MainActivity.this, ItemActivity.class);// MainActivity.this -> getApplicationContext()
                intent.putExtra("category_id", selected.getId());
                intent.putExtra("category_name", selected.getLabel());
                startActivity(intent);
            }
        };
        category.setOnItemClickListener(itemListener);
        bucket_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.d(TAG, "MainActivity: Floating Button clicked");
                notificationManager.notify(100, builder.build());
                Player1.start();
                Intent intent = new Intent(MainActivity.this, BasketActivity.class);// MainActivity.this -> getApplicationContext()
                startActivity(intent);
            }
        });

        dbHelper = new DBHelper(this);

    }
    private void createNotificationChannel(){
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O){
            CharSequence name = "discount";
            String description = "disc";
            int importance = NotificationManager.IMPORTANCE_DEFAULT;
            NotificationChannel channel = new NotificationChannel("asd", name, importance);
            channel.setDescription(description);
            NotificationManager notificationManager = getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }
    }
    private void setCategories(){
        Log.d(TAG, "MainActivity: set categories");
        DBAccess dbAccess = DBAccess.getInstance(getApplicationContext());
        dbAccess.open();
        categories = dbAccess.getCategories();
        dbAccess.close();
    }

    private void setPlayers(){
        Player1 = MediaPlayer.create(this, R.raw.bass);

    }
    public boolean onCreateOptionsMenu(Menu menu) {
        // this adds items to action bar
        getMenuInflater().inflate(R.menu.top_app_bar, menu);
        return true;
    }
}