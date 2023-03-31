//trying to make a post request for adding a new product
// import React, { useState } from 'react';

// const ProductForm = ({ onAddProduct }) => {
//   const [name, setName] = useState('');
//   const [price, setPrice] = useState('');
//   const [imageUrl, setImageUrl] = useState('');

  // const handleSubmit = async (event) => {
  //   event.preventDefault();
  //   try {
  //     const response = await fetch('http://127.0.0.1:5555/products', {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json',
  //       },
  //       body: JSON.stringify({ name, price, imageUrl }),
  //     });
  //     const data = await response.json();
  //     onAddProduct(data);
  //     setName('');
  //     setPrice('');
  //     setImageUrl('');
  //   } catch (error) {
  //     console.error(error);
  //   }
  // };

  // const handleSubmit = (event) => {
  //   event.preventDefault();
  //   const formData = new FormData(event.target);
  //   const data = {
  //     name: formData.get('name'),
  //     price: parseFloat(formData.get('price')),
  //     imageUrl: formData.get('imageUrl')
  //   };
  //   fetch('http://127.0.0.1:5555/add_product', {
  //     method: 'POST',
  //     headers: {
  //       'Content-Type': 'application/json'
  //     },
  //     body: JSON.stringify(data)
  //   })
  //   .then(response => response.json())
  //   .then(data => console.log(data))
  //   .catch(error => console.error(error));
  // }
  


import React, { useState } from 'react';

// const handleSubmit = (event) =>{
//   event.preventDefault();
//   if(data.password === data.confirmPassword){

//     const body ={
//       username: data.username,
//       email: data.email,
//       password: data.password
//     }
//     console.log(body)
    
//     fetch('http://localhost:5555/users',{
//       method: 'POST',
//       body: JSON.stringify(body),
//       headers:{
//         'content-type': 'application/json'
//       }
//     })

//     reset()
//     }

//   else{
//     alert("Passwords do not match")
//   }

// }

const ProductForm = ({ onAddProduct }) => {
  const [image, setImage] = useState('');
  const [name, setName] = useState('');
  const [price, setPrice] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const newProduct = {
      image:image,
      name:name,
      price:price,
    };

    console.log(newProduct)

    fetch("http://localhost:5555/category_products",{
      method: "POST",
      headers:{
        "Content-Type":"application/json",
      },
      body: JSON.stringify(newProduct),
    })


    //LOCALLY ADDING NEW PRODUCT
    // onAddProduct(newProduct);
    // setImage('');
    // setName('');
    // setPrice('');

    console.log(newProduct)
  };



  return (
    <div>
      <h2 className='addItemTitle'>Add an Item</h2>
      <form className='newProductForm' onSubmit={handleSubmit}>
        <label>
          Image URL:
          <input type="text" value={image} onChange={(e) => setImage(e.target.value)} />
        </label>
        <label>
          Name:
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        </label>
        <label>
          Price:
          <input type="text" value={price} onChange={(e) => setPrice(e.target.value)} />
        </label>
        <button type="submit">Add Product</button>
      </form>
    </div>
  );
};

export default ProductForm;
