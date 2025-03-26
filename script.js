
(function (){
    // Read from stdin
    process.stdin.on('data', (data) => {
        let category = data.toString();
        url = `https://opentdb.com/api.php?amount=5&category=${category}&difficulty=medium&type=multiple&encode=url3986`
        fetch(url)
        .then(res => res.json())
        .then(questions => console.log(JSON.stringify(questions)))
        .catch(
            err => 
            console.log(
                JSON.stringify(
                { "response_code":1, "ERROR": "An error occured while fetching data!...."}
                )
            )
        )
    });

})();
// (function (){
//     // Read from stdin
//     let category= process.stdin.on('data', (data) => {
//         console.log("data in  js",data.toString());
//                     return parseInt(data.toString()) 
//                 });
//     console.log(typeof category);
//     url = `https://opentdb.com/api.php?amount=5&category=${category}&difficulty=medium&type=multiple&encode=url3986`
//     fetch(url)
//     .then(res => res.json())
//     .then(questions => console.log(JSON.stringify(questions)))
//     .catch(
//         err => 
//         console.log(
//             JSON.stringify(
//             { "response_code":1, "ERROR": "An error occured while fetching data!...."}
//             )
//         )
//     )
// })();