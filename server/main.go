package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	router := gin.Default()

	router.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello World from Go server!",
		})
	})

	router.GET("/api/example", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "This is an example API endpoint.",
		})
	})

	router.Run(":9090")
}
