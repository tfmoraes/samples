package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
	)

func ReadPly(ply_filename string) func () (int, string) {
	ply_file, f_error := os.Open(ply_filename)
	reader := bufio.NewReader(ply_file)

	return func() (int, string) {
		if f_error != nil {
			return -1, ""
		}
		var status int
		var output string
		line, isPrefix, err := reader.ReadLine()
		switch {
		case err == os.EOF:
			status = 0
			output = ""
		case isPrefix:
			status = 1
			output = string(line)
			for ; isPrefix; {
				line, isPrefix, err = reader.ReadLine()
				output = output + string(line)
			}
		default:
			status = 1
			output = string(line)
		}
		return status, output
	}
}

func main() {
	ply_reader := ReadPly("/home/thiago/Meshes/dodecahedro.ply")
	var n_vertex, n_faces int
	for {
		status, line := ply_reader()

		if status == 0 { return }

		switch {
		case strings.HasPrefix(line, "element vertex"):
			n_vertex, _ = strconv.Atoi(strings.Split(line, " ")[2])
		case strings.HasPrefix(line, "element face"):
			n_faces, _ = strconv.Atoi(strings.Split(line, " ")[2])
		case strings.HasPrefix(line, "end_header"):
			break
		}
	}
	fmt.Println(n_vertex, n_faces)
}
