import { Categories } from './Categories';

export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  discountedPrice: null | number;
  formattedPrice?: any;
  img: string;
  category: Categories;
  stock: boolean;
  discount: null | number;
  featured: boolean;
}
