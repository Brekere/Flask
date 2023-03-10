<template>
    <h1>Listado de Productos</h1>

        <save-component 
        :key="product" 
        :productEdit="product" 
        @productInsert="productInsert" 
        @productUpdate="productUpdate"
        />

        <hr>

        <show-component :key="productShow" v-if="productShow != ''" :product="productShow"/>

        <div v-for="(p,i) in products.data" :key="p.id">
            <button @click="productEdit(p,i)">Editar</button>
            <button @click="productShow = p">Ver</button>
            <button @click="productDelete(p,i)">Eliminar</button>
            {{ p.name }}
        </div>

        <button @click="product=''">Crear</button>

</template>

<script>

import SaveComponent from "./SaveComponent"
import ShowComponent from "./ShowComponent"


export default{
    components:{
        SaveComponent,
        ShowComponent
    },
    data(){
        return{
            products:[],
            product: "",
            productShow:"",
            productIndex:0
        };
    },
    methods:{
        productInsert: function (product){
            console.log("Insertar producto")
            this.products.data.push(product)
        },
        productEdit: function(product, index){
            this.productIndex=index
            this.product=product
            console.log("Editar")
        },
        productDelete: function (product,index){
            if(confirm("Seguro que quieres eliminar el registro "+product.name)){
                this.products.data.splice(index,1)

                fetch('http://127.0.0.1:5000/api/products/'+product.id,{
                    method: 'DELETE'
                })
                .then(res => res.json())
                .then(res=> console.log(res))
            }
            
        },
        productUpdate: function(product){
            this.products.data[this.productIndex].name=product.name
            this.products.data[this.productIndex].category=product.category
            this.products.data[this.productIndex].category_id=product.category_id
            this.products.data[this.productIndex].price=product.price

        }
    },
    mounted(){
        fetch("http://127.0.0.1:5000/api/products/")
        .then((res) => res.json())
        .then((res) => this.products = res);
    }
}
</script>