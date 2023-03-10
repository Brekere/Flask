<template>
    <div v-if ="product">
        <h1>{{ product.data.name }}</h1>
        <p>{{ product.data.price }}</p>
        <p>{{ product.data.category }}</p>
    </div>
</template>

<script>

export default{
    props:{
        id:{
        required:true,
        type:Number
        }
    },
    data(){
        return {
            product:""
        }
    },
    mounted(){
        fetch("http://127.0.0.1:5000/api/products/"+this.id)
        .then((res)=>res.json())
        .then((res)=>(this.product=res))
    }
}

</script>