package main


import (
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"github.com/joho/godotenv"
	"os"
	"fmt"
	"time"
	"context"
)

func loadEnv() {
	err := godotenv.Load()
	if err != nil {
		fmt.Println("Error loading .env file")
	}
}


func connectToMongoDB() (*mongo.Client, error) {
	// Load environment variables from .env
	loadEnv()

	// Get MongoDB URI from environment variable
	mongodbURI := os.Getenv("MONGODB_URI")

	// Setting up MongoDB client options
	clientOptions := options.Client().ApplyURI(mongodbURI)

	// Create a MongoDB client
	client, err := mongo.NewClient(clientOptions)
	if err != nil {
		return nil, err
	}

	// Setting up a context with timeout
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	// Connect to MongoDB
	err = client.Connect(ctx)
	if err != nil {
		return nil, err
	}

	// Check the connection
	err = client.Ping(ctx, nil)
	if err != nil {
		return nil, err
	}

	fmt.Println("Connected to MongoDB!")
	return client, nil
}

func insertReport(client *mongo.Client, dbName, collectionName string, report Report) error {
	// Set up a context with timeout
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	// Get the database and collection
	db := client.Database(dbName)
	collection := db.Collection(collectionName)

	// Insert the report
	_, err := collection.InsertOne(ctx, report)
	return err
}
