package mainimport (



"context"



"fmt"



"log"



"protobuf-lesson/pb" "google.golang.org/grpc"



)// サーバーとの接続の確立



func main() {



conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure()) //SSL通信のオプションに変えるのが望ましい。



// エラーハンドリング



if err != nil {



log.Fatalf("Failed to connect: %v", err)



}



// main関数終了時にコネクションがクローズされるようにする



defer conn.Close() client := pb.NewFileServiceClient(conn)



callListFiles(client)



}func callListFiles(client pb.FileServiceClient) {



res, err := client.ListFiles(context.Background(), &pb.ListFilesRequest{})



if err != nil {



log.Fatalln(err)



} fmt.Println(res.GetFilenames())



}