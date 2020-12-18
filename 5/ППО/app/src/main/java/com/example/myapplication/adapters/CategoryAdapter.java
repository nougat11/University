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

import com.example.myapplication.R;
import com.example.myapplication.models.Category;

import java.util.List;

public class CategoryAdapter extends ArrayAdapter<Category> {

    private LayoutInflater inflater;
    private int layout;
    private List<Category> states;

    public CategoryAdapter(Context context, int resource, List<Category> states) {
        super(context, resource, states);
        this.states = states;
        this.layout = resource;
        this.inflater = LayoutInflater.from(context);
    }

    public View getView(int position, View convertView, ViewGroup parent) {

        Bitmap bitmap;

        CategoryAdapter.ViewHolder viewHolder;
        if(convertView==null){
            convertView = inflater.inflate(this.layout, parent, false);
            viewHolder = new CategoryAdapter.ViewHolder(convertView);
            convertView.setTag(viewHolder);
        }
        else{
            viewHolder = (CategoryAdapter.ViewHolder) convertView.getTag();
        }
        Category state = states.get(position);

        bitmap = BitmapFactory.decodeByteArray(state.getImageResource(), 0, state.getImageResource().length);
        viewHolder.imageView.setImageBitmap(bitmap);
        viewHolder.nameView.setText(state.getLabel());

        return convertView;
    }

    private class ViewHolder {
        final ImageView imageView;
        final TextView nameView;

        ViewHolder(View view){
            imageView = view.findViewById(R.id.categImage);
            nameView = view.findViewById(R.id.categName);
        }
    }

}
