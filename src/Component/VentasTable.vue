<template>
  <div class="table-responsive">
    
    <table class="table table-striped table-hover table-dark-custom d-none d-sm-table">
      <thead>
        <tr>
          <th class="py-2 px-4">Cliente / DNI</th>
          <th class="py-2 px-4">Oferta Aplicada</th>
          <th class="py-2 px-4">Teléfono</th>
          <th class="py-2 px-4">Fecha Reg.</th>
          <th class="py-2 px-4">Estado</th>
          <th class="py-2 px-4">Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="venta in ventas" :key="venta.id">
          <td class="py-3 px-4">{{ venta.cliente }}<br><span class="text-muted small">{{ venta.dni }}</span></td>
          <td class="py-3 px-4">{{ venta.oferta }}</td>
          <td class="py-3 px-4">{{ venta.telefono }}</td>
          <td class="py-3 px-4">{{ venta.fechaRegistro }}</td>
          <td class="py-3 px-4">
            <span :class="getStatusClass(venta.estado)" class="badge">
              {{ venta.estado }}
            </span>
          </td>
          <td class="py-3 px-4">
            <button @click="openDetails(venta)" class="btn btn-sm btn-olive me-2">Ver</button>
            <button @click="openSchedule(venta)" class="btn btn-sm btn-success">📅 Agendar</button>
          </td>
        </tr>
      </tbody>
      
      <tfoot>
        <tr>
            <td colspan="6" class="p-3 text-end text-muted small">
                1 - 10 de {{ ventas.length }} registros 
                <button class="btn btn-sm btn-dark ms-2">&lt;</button>
                <button class="btn btn-sm btn-dark">&gt;</button>
            </td>
        </tr>
      </tfoot>
      
    </table>

    <div class="d-sm-none space-y-3 p-3">
        </div>
  </div>
</template>

<script setup>
// Usamos JS Puro
import { defineProps } from 'vue';

defineProps({
  ventas: Array,
});

const getStatusClass = (estado) => {
  // Clases de Bootstrap y nuestra paleta de colores
  switch (estado) {
    case 'Venta Concretada':
      return 'bg-success'; 
    case 'Cancelada':
      return 'bg-secondary'; 
    case 'Agendada':
    case 'Pendiente por Móviles':
      return 'bg-info text-white'; 
    default:
      return 'bg-warning text-dark';
  }
};
// ... métodos openDetails y openSchedule
</script>

<style scoped>
/* Estilo para lograr la estética oscura */
.table-dark-custom {
    /* Fondo muy oscuro, similar al negro profundo */
    background-color: #2b2e32; 
    color: #f8f9fa; /* Texto blanco/gris claro */
}
/* Asegura que el hover y las líneas se vean bien */
.table-dark-custom tbody tr:hover {
    background-color: #3b3e42 !important;
}
/* ... otros estilos para el contraste ... */

/* Botón principal de acción en la tabla */
.btn-success {
    background-color: #4CAF50 !important;
    border-color: #4CAF50 !important;
}
/* Botón secundario/neutral en la tabla */
.btn-olive {
    background-color: #8D99AE; 
    border-color: #8D99AE;
    color: white;
}
</style>