package com.example.myapplication.models;

public class Category {
    private int id;
    private String label;
    private byte[] image;

    public Category(int id, String label, byte[] res){
        this.id = id;
        this.label = label;
        this.image = res;
    }

    public Category(String label, byte[] res){
        this.label = label;
        this.image = res;
    }

    public String getLabel() {
        return this.label;
    }

    public byte[] getImageResource() {
        return this.image;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}
