package com.example.myapplication.models;

public class Basket {
    private int id;
    private String name;
    private int amount;
    private byte[] image;
    private int price;
    private int id_item;
    public Basket(int id, String name, int amount, byte[] image, int price, int id_item){
        this.id = id;
        this.name = name;
        this.amount = amount;
        this.image = image;
        this.price = price;
        this.id_item = id_item;
    }
    public Basket(String name, int amount, byte[] image, int price, int id_item){
        this.name = name;
        this.amount = amount;
        this.image = image;
        this.price = price;
        this.id_item = id_item;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public byte[] getImage() {
        return image;
    }

    public void setImage(byte[] image) {
        this.image = image;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public int getId_item() {
        return id_item;
    }

    public void setId_item(int id_item) {
        this.id_item = id_item;
    }
}
