package com.company;

import java.sql.*;

public class InsertRecordIntoDb {
    public static void main(String[] args) {
        try {

            Connection con = null;
            Statement stmt = null;

            con = DriverManager
                    .getConnection("jdbc:sqlite:/C:\\sqlite\\java\\connect\\net\\sqlitetutorial\\Mulesoft\\MoviesDatabase.db");

            System.out.println("Database Connection Successful !!");

            stmt = con.createStatement(); // Create Statement

            String query0 = "INSERT INTO MyMovies values ('Bhool Bhulaiyaa 2','Kartik Aaryan','Kiara Advani',2022,'Anees Bazmee');";
            stmt.executeUpdate(query0); // Create Query-1

            String query1 = "INSERT INTO MyMovies values ('Jugjugg Jeeyo','Varun Dhawan','Kiara Advani',2022,'Raj Mehta');";
            stmt.executeUpdate(query1); // Create Query-1

            String query2 = "INSERT INTO MyMovies values ('Baaghi 3','Tiger Shroff','Shraddha Kapoor',2020,'Ahmed Khan');";
            stmt.executeUpdate(query2); // Create Query-2

            String query3 = "INSERT INTO MyMovies values ('Jersey','Shahid Kapoor','Mrunal Thakur',2022,'Gowtam Tinnanuri');";
            stmt.executeUpdate(query3); // Create Query-3

            String query4 = "INSERT INTO MyMovies values ('Shershaah','Sidharth Malhotra','Kiara Advani',2021,'Vishnuvardhan');";
            stmt.executeUpdate(query4); // Create Query-4
            stmt.close();

            con.close();                //Close Connection
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
            System.exit(0);
        }
        System.out.println("Record  Insertion successful");
    }
}