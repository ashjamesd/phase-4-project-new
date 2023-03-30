import React, {useState} from 'react';
import ProductForm from './ProductForm';
import ProductList from './ProductList';
import Cart from './Cart';

const Home = () => {

  const onAddProduct = (product) => {
    setProducts([...products, product]);
  };

  const onAddToCart = (product) =>{
    console.log(`${product.name} added to cart`);
  };

  const [cartItems, setCartItems] = useState(['']);

  const addToCart = (product) => {
    setCartItems((prevCartItems) => [...prevCartItems, product])};


  const [products, setProducts] = useState([
    { id: 1, imageUrl: 'https://picsum.photos/200/300', name: 'Product 1', price: 10 },
    { id: 2, imageUrl: 'https://picsum.photos/200/300', name: 'Product 2', price: 20 },
    { id: 3, imageUrl: 'https://picsum.photos/200/300', name: 'Product 3', price: 30 },
  ]);

  return (
    <div>
      <h1>Home Component</h1>
      <ProductList products={products} onAddToCart={addToCart} />
      <ProductForm onAddProduct={onAddProduct} />
      <Cart cartItems={cartItems} />
      
    </div>
  );
};

export default Home;
