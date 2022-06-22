export interface Product{
    id: number,
    name: string;
    description: string;
    price: number;
    filename: string;
    rating: number;
    count:number;
    shop:string;
}

export interface Category{
    id: number;
    name: string;
}

export interface Shop{
    id: number;
    name: string;
    description: string;
}

export interface City{
    id: number;
    name: string;
}

export interface AuthToken {
    token: string;
}
