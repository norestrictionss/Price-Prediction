const express=require('express')
const path=require('path')
const app=express()
const admin=require("./public/admin")
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static('./public'))




app.get('/', (req, res)=>{



})


app.post('/main', (req, res)=>{


    const username=req.body.username
    const password=req.body.password

    
    if(username===admin.username && password===admin.password){
        
        res.sendFile(path.join(__dirname, '/main.html'))
        res.sendFile(path.join(__dirname, '/style.css'))
        console.log(path.join(__dirname, '/style.css'))
        console.log(path.join(__dirname, '/main.html'))
        res.end()
    }
        
   
    else console.log('Wrong! Please try again')
})


app.listen(5000, ()=>{

    

})