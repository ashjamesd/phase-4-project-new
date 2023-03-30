// import React from 'react';

// const ProductList = ({ products, onAddToCart }) => {
//   return (
//     <div>
//       <h2>Featured Products</h2>
//       {products.map((product) => (
//         <div key={product.id}>
//           <img src={product.imageUrl} alt={product.name} />
//           <h3>{product.name}</h3>
//           <p>{product.price}</p>
//           <button onClick ={()=>onAddToCart(product)}>Add to Cart</button>

//         </div>
//       ))}
//     </div>
//   );
// };

// export default ProductList;

import React, { useState, useEffect } from 'react';

const ProductList = ({ onAddToCart }) => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    async function fetchProducts() {
      const response = await fetch('http://localhost:3000/products');
      const data = await response.json();
      setProducts(data);
    }
    fetchProducts();
  }, []);

  return (
    <div>
      <h2>Featured Products</h2>
      {products.map((product) => (
        <div key={product.id}>
          <img className='productImage' src={product.image} alt={product.name} />
          <h3>{product.name}</h3>
          <p>{product.price}</p>
          <button onClick={() => onAddToCart(product)}>Add to cart</button>
        </div>
      ))}
    </div>
  );
};

export default ProductList;
