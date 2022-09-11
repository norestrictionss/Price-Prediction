express=require('express')

home_router=require('./routes/home')
about_router=require('./routes/about')

app=express()

// Middlewares
app.use(home_router, express.static('./public'))
app.use(about_router)




app.listen(5000)