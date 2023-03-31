import React, {useState} from 'react';
import {Form, Button} from 'react-bootstrap'

const Login = () => {

  const [username, setUsername]=useState('')
  const[password, setPassword]=useState('')

  const loginUser=()=>{
    console.log(username)
    console.log(password)

    setUsername('')
    setPassword('')
  }

  return (
    <div className='loginContainer'>
      <div className='loginForm'>
        <h1>Login Page</h1>
        <form>
          <Form.Group>
            <Form.Label>Username</Form.Label>
            <Form.Control type = "text" placeholder="Enter Usename" value={username} onChange={(e)=>{setUsername(e.target.value)}} name="username"/>
          </Form.Group>
  
          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control type = "password" placeholder="Enter Password" value={password} onChange={(e)=>{setPassword(e.target.value)}} name="password"/>
          </Form.Group>

          <Form.Group>
            <Button varient="primary" onClick={loginUser}>Login</Button>
          </Form.Group>
        </form>
    </div>
  </div>
  );
};

export default Login;
