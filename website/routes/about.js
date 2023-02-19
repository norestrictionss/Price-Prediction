express=require('express')
path=require('path')
router=express.Router()

router.get('/about', (req, res)=>{
    
       res.sendFile(path.join(__dirname, '../public/main.html'))
})

module.exports=router