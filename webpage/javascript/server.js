const express = require('express')

const app = express()
const cors = require('cors');

const mysql = require('mysql2');



const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: '123456789',
  database: 'fuel_station'
}).promise()


app.use(cors());




async function getLogs(query) {
    try {
    const [rows] = await pool.query(query);
    
    return rows;
    } catch{error}{
        console.log("error trying to access the db")
    }
};     




app.get('/count', async (req,res) => {
    try {
        const query = "select message as data,count(message) as count from logs where message in ('start','f95','diesel') group by message";
        const result = await getLogs(query);
        res.json(result);
    } catch (error){
    console.error(error);
    res.status(500).json({error:'Error'})
    }
});

app.get('/location', async (req,res) => {
    try {

        const query = 'SELECT name as data, count(name) as count FROM ccaa_register as r inner join ccaa as c on c.id_ccaa=r.location_id group by name';
        const result = await getLogs(query);
        res.json(result);
        
    } catch (error){
    console.error(error);
    res.status(500).json({error:'Error'})
    }
});

app.get('/mostused', async (req,res) => {
    try {
         
        const query = "SELECT date(msg_date) as data,count(msg_date) as count from logs where message in ('f95','diesel') group by date(msg_date) order by count(msg_date) desc limit 6;";
        const result = await getLogs(query);
        const modifiedResult = result.map(row=>{
            row.data = row.data.toISOString();
            row.data = row.data.split('T')[0];
            return row;
        });

        res.json(modifiedResult) 

} catch (error){
    console.error(error);
    res.status(500).json({error:'Error'})
}
});



app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
  });
  
const port = process.env.PORT || 5000;

app.listen(port,() => {
    console.log('Server is running on port '+ port);
});



app.on('warning', (warning) => {
    console.log(warning.stack);
});







