package com.example.myapplication.models;

public class Item {
    private int id;
    private String name;
    private byte[] image;
    private int price;
    private int category;
    private boolean isViewed;
    private String description = "Купи или бан.";

    public Item(){}
    public Item (int id, String name, byte[] image, int price, int category, boolean isViewed){
        this.id = id;
        this.name = name;
        this.image = image;
        this.price = price;
        this.category = category;
        this.isViewed = isViewed;
    }
    public Item (String name, byte[] image, int price, int category){
        this.name = name;
        this.image = image;
        this.price = price;
        this.category = category;
        this.isViewed = false;
    }
    public int getId(){return this.id;}
    public int setId(int id){return this.id = id;}
    public String getName(){return this.name;}
    public String setName(String name){return this.name = name;}
    public byte[] getImage(){return this.image;}
    public byte[] setImage(byte[] image){return this.image = image;}
    public int getPrice(){return this.price;}
    public int setPrice(int price){return this.price = price;}
    public int getCategory(){return this.id;}
    public int setCategory(int category){return this.category = category;}
    public boolean getView(){return this.isViewed;}
    public boolean setView(boolean isViewed){return this.isViewed = isViewed;}
    public String getDescription(){return this.description;}
    public String setDescrition(String description){return this.description = description;}

}
