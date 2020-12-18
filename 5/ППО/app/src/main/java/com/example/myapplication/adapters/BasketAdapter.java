package com.example.myapplication.adapters;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.MediaPlayer;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.myapplication.R;
import com.example.myapplication.SwipeListener;
import com.example.myapplication.db.DBAccess;
import com.example.myapplication.db.DBHelper;
import com.example.myapplication.models.Basket;

import java.util.List;

public class BasketAdapter extends ArrayAdapter<Basket> {
    SwipeListener SwipeListener;
    //
    private LayoutInflater inflater;
    private int layout;
    private List<Basket> itemList;
    private DBHelper dbHelper;

    public BasketAdapter(Context context, int resource, List<Basket> itemList) {
        super(context, resource, itemList);
        this.itemList = itemList;
        this.layout = resource;
        this.inflater = LayoutInflater.from(context);

        dbHelper = new DBHelper(context);
    }

    public View getView(final int position, View convertView, ViewGroup parent) {

        Bitmap bitmap;

        final BasketAdapter.ViewHolder viewHolder;
        if(convertView==null){
            convertView = inflater.inflate(this.layout, parent, false);
            viewHolder = new BasketAdapter.ViewHolder(convertView);
            convertView.setTag(viewHolder);
        }
        else{
            viewHolder = (BasketAdapter.ViewHolder) convertView.getTag();
        }
        final Basket basketModel = itemList.get(position);

        bitmap = BitmapFactory.decodeByteArray(basketModel.getImage(), 0, basketModel.getImage().length);
        viewHolder.imageView.setImageBitmap(bitmap);
        viewHolder.nameTextView.setText(basketModel.getName());
        viewHolder.priceTextView.setText(String.valueOf(basketModel.getPrice()) + "$");
        viewHolder.amountTextView.setText(String.valueOf(basketModel.getAmount()));

        viewHolder.imageButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                DBAccess dbAccess = DBAccess.getInstance(getContext());
                dbAccess.open();
                dbAccess.putItemInBasket(itemList.get(position));
                dbAccess.close();
                basketModel.setAmount(basketModel.getAmount() + 1);
                viewHolder.amountTextView.setText(String.valueOf(basketModel.getAmount()));
            }
        });
        viewHolder.removeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                DBAccess dbAccess = DBAccess.getInstance(getContext());
                dbAccess.open();
                dbAccess.removeItemFromBasket(itemList.get(position).getId());
                dbAccess.close();
                itemList.remove(position);
                BasketAdapter.this.notifyDataSetChanged();
            }
        });

        SwipeListener = new SwipeListener(getContext()) {
            @Override
            public void onSwipeRight() {
                Toast.makeText(getContext(), itemList.get(position).getName() + " right", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onSwipeLeft() {
                Toast.makeText(getContext(), itemList.get(position).getName() + " left", Toast.LENGTH_SHORT).show();
                DBAccess dbAccess = DBAccess.getInstance(getContext());
                dbAccess.open();
                dbAccess.removeItemFromBasket(itemList.get(position).getId());
                dbAccess.close();
                final MediaPlayer mediaPlayer2 = MediaPlayer.create(getContext(), R.raw.bass_click);
                mediaPlayer2.start();
                itemList.remove(position);
                BasketAdapter.this.notifyDataSetChanged();
            }
        };
        convertView.setOnTouchListener(SwipeListener);


        return convertView;
    }

    private class ViewHolder {
        final TextView nameTextView;
        final TextView amountTextView;
        final ImageView imageView;
        final TextView priceTextView;
        final ImageButton imageButton;
        final ImageButton removeButton;

        ViewHolder(View view){
            imageView = view.findViewById(R.id.basketImage);
            nameTextView = view.findViewById(R.id.basketName);
            amountTextView = view.findViewById(R.id.basketAmount);
            priceTextView = view.findViewById(R.id.basketPrice);
            imageButton = view.findViewById(R.id.basketBtn);
            removeButton = view.findViewById(R.id.removeBasketBtn);
        }
    }

}
