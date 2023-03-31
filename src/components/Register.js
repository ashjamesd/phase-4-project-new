
import React, {useState} from 'react';
import {Form, Button, Alert} from 'react-bootstrap'
import { Links } from 'react-router-dom'
import {useForm} from 'react-hook-form'
// import { toHaveErrorMessage } from '@testing-library/jest-dom/dist/matchers';
// import { error } from '@babel/eslint-parser/lib/convert/index.cjs';



const Register = () => {
  // const[username,setUsername]=useState('')
  // const[email,setEmail]=useState('')
  // const[password,setPassword]=useState('')
  // const[confirmPassword,setConfirmPassword]=useState('')

  const{register, watch, reset, handleSubmit,formState:{errors}} = useForm();

// const username = '';
// const email = '';
// const password= '';
// const confirmPassword = '';

const submitForm = (data) =>{
  if(data.password === data.confirmPassword){

    const body ={
      username: data.username,
      email: data.email,
      password: data.password
    }    

    const requestOptions={
      methods: "POST",
      headers:{
        'content-type':'application/json'
      },
      body:JSON.stringify(body)
    }

    fetch('http://localhost:5555/users', requestOptions)
    .then(response=>response.json())
    .then(data=>console.log(data))

    reset()
    }

  else{
    alert("Passwords do not match")
  }

}

// console.log(watch("username"));

  return (
    <div className='signupContainer'>
      <div className='signupForm'>
        <h1>Sign Up</h1>
        <form>
          <Form.Group>
            <Form.Label>Username</Form.Label>
            <Form.Control type = "text" placeholder="Enter Usename" {...register("username",{required:true, maxLength:25})}/>
          </Form.Group>
          {errors.username && <span style={{color:'red'}}>Username is required</span>}
          <br></br>
          {errors.username?.type==="maxLength"&&<span style={{color: "red"}}>Username cannot be longer than 25 characters</span>}
          <Form.Group>
            <Form.Label>Email</Form.Label>
            <Form.Control type = "email" placeholder="Enter email" {...register("email",{required:true, maxLength: 80})}/>
          </Form.Group>
          {errors.email && <span style={{color:'red'}}>Email is required</span>}
          <br></br>
          {errors.username?.type==="maxLength"&&<span style={{color: "red"}}>Email cannot be longer than 80 characters</span>}
          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control type = "password" placeholder="Enter Password" {...register("password",{required:true, minLength: 8})}/>
          </Form.Group>
          {errors.password && <span style={{color:'red'}}>Password is required</span>}
          <br></br>
          {errors.password?.type==="minLength"&&<span style={{color: "red"}}>Password must be at least 8 characters</span>}
          <Form.Group>
            <Form.Label>Confirm Password</Form.Label>
            <Form.Control type = "password" placeholder="Enter Password" {...register("confirmPassword",{required:true, minLength: 8})}/>
          </Form.Group>
          {errors.confirmPassword && <span style={{color:'red'}}>Password Confirmation is required</span>}
          <br></br>
          {errors.confirmPassword?.type==="minLength"&&<span style={{color: "red"}}>Password must be at least 8 characters</span>}

          <Form.Group>
            <Button varient="primary" onClick={handleSubmit(submitForm)}>Register</Button>
          </Form.Group>
        </form>
    </div>
  </div>
  );

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState(false);

  const handleName = (e) => {
    setName(e.target.value);
    setSubmitted(false);
  };

  const handleEmail = (e) => {
    setEmail(e.target.value);
    setSubmitted(false);
  };

  const handlePassword = (e) => {
    setPassword(e.target.value);
    setSubmitted(false);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (name === "" || email === "" || password === "") {
      setError(true);
    } else {
      setSubmitted(true);
      setError(false);
    }
  };

  const successMessage = () => {
    return (
      <div
        className="success"
        style={{
          display: submitted ? "" : "none",
        }}
      >
        <h1>User {name} successfully registered!!</h1>
      </div>
    );
  };

  const errorMessage = () => {
    return (
      <div
        className="error"
        style={{
          display: error ? "" : "none",
        }}
      >
        <h1>Please enter all the fields</h1>
      </div>
    );
  };

  return (
    <div className="form">
      <div>
        <h1>User Registration</h1>
      </div>

      <div className="messages">
        {errorMessage()}
        {successMessage()}
      </div>

      <form>
        <label className="label">Name</label>
        <input
          onChange={handleName}
          className="input"
          value={name}
          type="text"
        />

        <label className="label">Email</label>
        <input
          onChange={handleEmail}
          className="input"
          value={email}
          type="email"
        />

        <label className="label">Password</label>
        <input
          onChange={handlePassword}
          className="input"
          value={password}
          type="password"
        />

        <button onClick={handleSubmit} className="btn" type="submit">
          Submit
        </button>
      </form>
    </div>
  );
};

export default Register;
