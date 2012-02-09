package main

import (
    "fmt"
    "os"
    "syscall"
    "unsafe"
    "time"
)

func main() {
    const n = 1e2
    t := int(unsafe.Sizeof(float64(0.0))) * n * 3

    map_file, err := os.Create("/tmp/test.dat")
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
    _, err = map_file.Seek(int64(t-1), 0)
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
    _, err = map_file.Write([]byte(" "))
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }

    mmap, _ := syscall.Mmap(map_file.Fd(), 0, int(t), syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_SHARED)
    /*if err != nil {*/
        /*fmt.Println(err)*/
        /*os.Exit(1)*/
    /*}*/
    map_array := (*[n][3]float64)(unsafe.Pointer(&mmap[0]))

    for i := 0; i < n; i++ {
        map_array[i][0] = float64(i * i)
        map_array[i][1] = float64(i * i) + 1
        map_array[i][2] = float64(i * i) + 2
    }

    fmt.Println(map_array)

    _ = syscall.Munmap(mmap)
    /*if err != nil {*/
        /*fmt.Println(err)*/
        /*os.Exit(1)*/
    /*}*/
    err = map_file.Close()
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
    time.Sleep(10000000000)
}
