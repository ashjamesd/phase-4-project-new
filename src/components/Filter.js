import React, { useState } from 'react';

const ProductFilter = ({ products, onFilterChange }) => {
  const [selectedValue, setSelectedValue] = useState('');

  const handleFilterChange = (event) => {
    const value = event.target.value;
    setSelectedValue(value);
    onFilterChange(value);
  };

  const uniqueNames = Array.from(new Set(products.map((product) => product.name)));

  return (
    <div>
      <label htmlFor="filter">Filter by name:</label>
      <select id="filter" value={selectedValue} onChange={handleFilterChange}>
        <option value="">All products</option>
        {uniqueNames.map((name) => (
          <option key={name} value={name}>
            {name}
          </option>
        ))}
      </select>
    </div>
  );
};

export default ProductFilter;
