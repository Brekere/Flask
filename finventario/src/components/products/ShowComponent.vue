<template>
        <h1>{{ product.name }}</h1>
        <p>{{ product.price }}</p>
        <p>{{ product.category }}</p>
</template>

<script>

export default{
    props:{
        product:{
            required: true,
            type: Object
        }
    }
}


</script>