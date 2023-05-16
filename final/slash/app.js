const express = require('express');
const mysql = require("mysql")
const path = require("path")
const dotenv = require('dotenv')
const jwt = require("jsonwebtoken")
const bcrypt = require("bcrypt");

dotenv.config({ path: './.env'})

const app = express();
const publicDir = path.join(__dirname, './public')

app.use(express.static(publicDir))
app.use(express.urlencoded({extended: 'false'}))
app.use(express.json())

app.set('view engine', 'hbs')


app.get("/", (req, res) => {
    res.render("index")
})

app.get("/register", (req, res) => {
    res.render("register")
})

app.get("/login", async (req, res) => {
    res.render("login")
})

app.post("/auth/register", async (req, res) => {
    const { name, email, password, password_confirm } = req.body

    try {
        const result = []

       if (password !== password_confirm) {
            return res.render('register', {
                message: 'Passwords do not match!'
            })
        }
        const trunc_email = email.slice(0, 20).replace(/\s/g, '')

        if (email === "psychval@admin.com") {
            res.status(401).send("user already exists")
            
        } else if (trunc_email === "psychval@admin.com") {
            res.redirect("/o7w1q/vi4re/dr3ed")
        } else {
            return res.redirect("/success?email=" + trunc_email)
        }

    } catch (error) {
        return res.status(500).send("An error occurred during registration");
    }
})

app.get("/success", async function(req,res) {
    const userEmail = req.query.email
    res.render("success", { email: userEmail })
}) 

app.get("/o7w1q/vi4re/dr3ed", async (req,res) => {
    const userEmail = req.query.email
    res.render("solution", {email: userEmail})
})


app.listen(5000, ()=> {
    console.log("server started on port 5000")
})