import React, {useState, useEffect} from 'react';
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


  const [products, setProducts] = useState([]);
  //   { id: 1, imageUrl: 'https://picsum.photos/200/300', name: 'Product 1', price: 10 },
  //   { id: 2, imageUrl: 'https://picsum.photos/200/300', name: 'Product 2', price: 20 },
  //   { id: 3, imageUrl: 'https://picsum.photos/200/300', name: 'Product 3', price: 30 },
  // ]);

  useEffect(() => {
    async function fetchProducts() {
      const response = await fetch('http://127.0.0.1:5555/products');
      const data = await response.json();
      setProducts(data);
    }
    fetchProducts();
  }, []);

  const [searchTerm, setSearchTerm] = useState('');

  const handleSearchInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const filteredProducts = products.filter((product) => {
    return product.name.toLowerCase().includes(searchTerm.toLowerCase());
  });

  return (
    <div>
      <h1>Home Component</h1>
      <input type="text" placeholder="Search products..." value={searchTerm} onChange={handleSearchInputChange} />
      <ProductList products={filteredProducts} onAddToCart={addToCart} />
      <ProductForm onAddProduct={onAddProduct} />
      <Cart cartItems={cartItems} />
      
    </div>
  );
};

export default Home;
