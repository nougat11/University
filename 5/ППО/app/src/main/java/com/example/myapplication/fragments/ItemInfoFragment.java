package com.example.myapplication.fragments;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.example.myapplication.R;
import com.example.myapplication.models.Item;
import com.github.chrisbanes.photoview.PhotoView;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link ItemInfoFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class ItemInfoFragment extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    final static String TAG = "ALIEXPRESS";
    private static final String ARG_ITEM_IMAGE = "ARG_ITEM_IMAGE";
    private static final String ARG_ITEM_NAME =  "ARG_ITEM_NAME";
    private static final String ARG_ITEM_PRICE = "ARG_ITEM_PRICE";
    private static final String ARG_ITEM_DESC =  "ARG_ITEM_DESC";

    // TODO: Rename and change types of parameters
    private byte[] Image;
    private String Name;
    private String Description;
    private int Price;
    private PhotoView itemImageView;
    private TextView nameTextView;
    private TextView priceTextView;
    private TextView descriptionTextView;

    public ItemInfoFragment() {
        // Required empty public constructor
    }


    // TODO: Rename and change types and number of parameters
    public static ItemInfoFragment newInstance(String name, byte[] image, int price, String desc) {
        Log.d(TAG, "ItemInfoFragment newInstance");
        ItemInfoFragment fragment = new ItemInfoFragment();
        Bundle args = new Bundle();
        args.putByteArray(ARG_ITEM_IMAGE, image);
        args.putString(ARG_ITEM_NAME, name);
        args.putInt(ARG_ITEM_PRICE, price);
        args.putString(ARG_ITEM_DESC, desc);
        fragment.setArguments(args);
        return fragment;
    }
    public void updateValues(Item item){
        Bitmap bitmap = BitmapFactory.decodeByteArray(item.getImage(), 0, item.getImage().length);
        itemImageView.setImageBitmap(bitmap);
        nameTextView.setText(item.getName());
        String s = String.valueOf(item.getPrice()) + '$';
        priceTextView.setText(s);
        descriptionTextView.setText(item.getDescription()); // item.getDescription()
        Log.d(TAG, "ItemInfoFragment updateValues done");
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d(TAG, "ItemInfoFragment onCreate");
        if (getArguments() != null) {
            if (getArguments() != null){
                this.Image = getArguments().getByteArray(ARG_ITEM_IMAGE);
                this.Name = getArguments().getString(ARG_ITEM_NAME);
                this.Price = getArguments().getInt(ARG_ITEM_PRICE);
                this.Description = getArguments().getString(ARG_ITEM_DESC);
                Log.d(TAG, "ItemInfoFragment onCreate 4 vars set");
            }
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        Log.d(TAG, "ItemInfoFragment onCreateView start");
        View view = inflater.inflate(R.layout.fragment_item_info, container, false);
        itemImageView = view.findViewById(R.id.item_image_view);
        nameTextView = view.findViewById(R.id.item_name_text_view);
        priceTextView = view.findViewById(R.id.item_price_text_view);
        descriptionTextView = view.findViewById(R.id.item_description_text_view);
        if (getArguments() != null)
        {
            System.out.println("Arguments not null!");
        }
        else{
            System.out.println("Arguments  NULL!");
        }
        Bitmap bitmap = BitmapFactory.decodeByteArray(Image, 0, Image.length);
        itemImageView.setImageBitmap(bitmap);
        nameTextView.setText(Name);
        String s = String.valueOf(Price) + '$';
        priceTextView.setText(s);
        descriptionTextView.setText(Description);
        return view;
    }
}