
express=require('express')
router=express.Router()


router.get('/', (req, res)=>{

    res.status(200).send('Home')


})

module.exports=router