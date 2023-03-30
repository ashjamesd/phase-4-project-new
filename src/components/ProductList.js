import React from 'react';

const ProductList = ({ products }) => {
  return (
    <div>
      <h2>Featured Products</h2>
      {products.map((product) => (
        <div key={product.id}>
          <img src={product.imageUrl} alt={product.name} />
          <h3>{product.name}</h3>
          <p>{product.price}</p>
        </div>
      ))}
    </div>
  );
};

export default ProductList;
