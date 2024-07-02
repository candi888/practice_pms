use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let f = File::open("./src/hello1.txt").unwrap();
    println!("{:?}", f);
    std::process::exit(0);

    // let f = match f {
    //     Ok(file) => file,
    //     Err(ref error) if error.kind() == ErrorKind::NotFound => {
    //         match File::create("./src/hello.txt") {
    //             Ok(fc) => fc,
    //             Err(e) => {
    //                 panic!(
    //                     //ファイルを作成しようとしましたが、問題がありました
    //                     "Tried to create file but there was a problem: {:?}",
    //                     e
    //                 )
    //             }
    //         }
    //     }
    //     Err(error) => {
    //         panic!("There was a problem opening the file: {:?}", error)
    //     }
    // };
}
