<template>
    <h1>Registrar Productos</h1>

<form @submit="sendForm">
    <label for="">Nombre</label>
    <input type="text" v-model="product.name">
    <br>
    <label for="">Precio</label>
    <input type="number" v-model="product.price">
    <br>
    <label for="">Categoria</label>
    <select v-model="product.category_id">
        <option v-for="c in categories.data" :key="c.id" :value="c.id">
            {{ c.name }}
        </option>
    </select>
    <input type="submit" value="Enviar">

</form>


</template>

<script>
export default {
    props: ['productEdit'],
    emits: ['productInsert','productUpdate'],
    data(){
        return{
            categories:[],
            product:{
                name:"",
                price:"",
                category_id:""
            }

        }
    },
    methods: {
        sendForm(e){
            e.preventDefault();
            
                console.log(this.product)

            const formData =new FormData()

            formData.append('name',this.product.name)
            formData.append('category_id',this.product.category_id)
            formData.append('price',this.product.price)

        if (this.productEdit == "")    
            this.insert(formData)
            else
            this.update(formData)
                

        },
        insert (formData){
            fetch("http://127.0.0.1:5000/api/products/",{
                method: 'POST',
                body: formData
            })
                .then((res) => res.json())
                .then((product) => this.$emit("productInsert",product.data)              
                );
        },
        update (formData){
            fetch("http://127.0.0.1:5000/api/products/"+this.productEdit.id,{
                method: 'PUT',
                body: formData
            })
                .then((res) => res.json())
                .then((product) => this.$emit("productUpdate",product.data)              
                );
        },
    },
    mounted(){
        if(this.productEdit!=""){
            this.product.name = this.productEdit.name
            this.product.price = this.productEdit.price
            this.product.category_id = this.productEdit.category_id
            console.log("Editar");
        }
            

        fetch("http://127.0.0.1:5000/api/categories/")
        .then((res) => res.json())
        .then((res) => this.categories = res);
    }
}
</script>