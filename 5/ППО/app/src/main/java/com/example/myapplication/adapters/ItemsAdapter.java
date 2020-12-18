package com.example.myapplication.adapters;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.core.content.ContextCompat;

import com.example.myapplication.R;
import com.example.myapplication.models.Item;

import java.util.List;

public class ItemsAdapter extends ArrayAdapter<Item> {
    private LayoutInflater inflater;
    private int layout;
    private List<Item> itemList;
    public ItemsAdapter(Context context, int resource, List<Item> itemList) {
        super(context, resource, itemList);
        this.itemList = itemList;
        this.layout = resource;
        this.inflater = LayoutInflater.from(context);
    }
    public View getView(int position, View convertView, ViewGroup parent) {

        Bitmap bitmap;

        ItemsAdapter.ViewHolder viewHolder;
        if(convertView==null){
            convertView = inflater.inflate(this.layout, parent, false);
            viewHolder = new ItemsAdapter.ViewHolder(convertView);
            convertView.setTag(viewHolder);
        }
        else{
            viewHolder = (ItemsAdapter.ViewHolder) convertView.getTag();
        }
        Item state = itemList.get(position);

        bitmap = BitmapFactory.decodeByteArray(state.getImage(), 0, state.getImage().length);
        viewHolder.imageView.setImageBitmap(bitmap);
        viewHolder.nameTextView.setText(state.getName());
        viewHolder.priceTextView.setText(String.valueOf(state.getPrice()) + "$");
        if (state.getView()) //Если элемент уже просмотрен
            viewHolder.nameTextView.setTextColor(ContextCompat.getColor(getContext(), android.R.color.holo_red_dark));
        else
            viewHolder.nameTextView.setTextColor(ContextCompat.getColor(getContext(), android.R.color.black));

        return convertView;
    }

    private class ViewHolder {
        final TextView nameTextView;
        final ImageView imageView;
        final TextView priceTextView;

        ViewHolder(View view){
            imageView = view.findViewById(R.id.itemImage);
            nameTextView = view.findViewById(R.id.itemName);
            priceTextView = view.findViewById(R.id.itemPrice);
        }
    }
}
