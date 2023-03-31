import React, {useState} from 'react';
import {Form, Button, Alert} from 'react-bootstrap'
import { LinkS } from 'react-router-dom'
import {useForm} from 'react-hook-form'
// import { toHaveErrorMessage } from '@testing-library/jest-dom/dist/matchers';
// import { error } from '@babel/eslint-parser/lib/convert/index.cjs';


const Register = () => {
  // const[username,setUsername]=useState('')
  // const[email,setEmail]=useState('')
  // const[password,setPassword]=useState('')
  // const[confirmPassword,setConfirmPassword]=useState('')

  const{register, watch, handleSubmit,formState:{errors}} = useForm();

// const username = '';
// const email = '';
// const password= '';
// const confirmPassword = '';

const submitForm = (data) =>{
  console.log(data)
}

console.log(watch("username"));

  return (
    <div className='signupContainer'>
      <div className='signupForm'>
        <h1>Sign Up Page</h1>
        <form>
          <Form.Group>
            <Form.Label>Username</Form.Label>
            <Form.Control type = "text" placeholder="Enter Usename" {...register("username",{required:true, maxLength:25})}/>
          </Form.Group>
          {errors.username && <span style={{color:'red'}}>Username is required</span>}
          <br></br>
          {errors.username?.type=="maxLength"&&<span style={{color: "red"}}>Username cannot be longer than 25 characters</span>}
          <Form.Group>
            <Form.Label>Email</Form.Label>
            <Form.Control type = "email" placeholder="Enter email" {...register("email",{required:true, maxLength: 80})}/>
          </Form.Group>
          {errors.email && <span style={{color:'red'}}>Email is required</span>}
          <br></br>
          {errors.username?.type=="maxLength"&&<span style={{color: "red"}}>Email cannot be longer than 80 characters</span>}
          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control type = "password" placeholder="Enter Password" {...register("password",{required:true, minLength: 8})}/>
          </Form.Group>
          {errors.password && <span style={{color:'red'}}>Password is required</span>}
          <br></br>
          {errors.password?.type=="minLength"&&<span style={{color: "red"}}>Password must be at least 8 characters</span>}
          <Form.Group>
            <Form.Label>Confirm Password</Form.Label>
            <Form.Control type = "password" placeholder="Enter Password" {...register("confirmPassword",{required:true, minLength: 8})}/>
          </Form.Group>
          {errors.confirmPassword && <span style={{color:'red'}}>Password Confirmation is required</span>}
          <br></br>
          {errors.confirmPassword?.type=="minLength"&&<span style={{color: "red"}}>Password must be at least 8 characters</span>}

          <Form.Group>
            <Button varient="primary" onClick={handleSubmit(submitForm)}>Register</Button>
          </Form.Group>
        </form>
    </div>
  </div>
  );
};

export default Register;
