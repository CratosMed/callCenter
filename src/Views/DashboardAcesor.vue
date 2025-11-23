<script setup>
// 1. IMPORTACIÓN: Usas la ruta relativa para traer el componente
import VentasTable from '../Component/VentasTable.vue'; 
// ...
</script>

<template>
    <VentasTable :ventas="filteredVentas" /> 
</template>