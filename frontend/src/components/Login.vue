<template>
<div class='tasks'>  

    <b-table striped hover 
        responsive="sm"
        :items="tasks" 
        :fields="fields">
        
        <template #cell(actions)="row" >
            <b-button variant="danger" size="sm" @click="deleteTask(row.item)" class="mr-2">
                Remove
            </b-button>
        </template>
    </b-table>   

    <h2>Tasks</h2>
    <b-form inline @submit="addTask">
        <label class="sr-only" for="inline-form-input-name">Title</label>
        <b-form-input v-model='newTask.title'
            id="inline-form-input-name"
            class="mb-2 mr-sm-2 mb-sm-0"
            placeholder="Add title"
        ></b-form-input>

        <label class="sr-only" for="inline-form-input-username">Description</label>
        <b-form-input v-model='newTask.description'
            id="inline-form-input-name"
            class="mb-2 mr-sm-2 mb-sm-0"
            placeholder="Add description"
        ></b-form-input>
        <br>        
        <b-button type="submit" variant="success">Submit</b-button>
    </b-form>
</div>
</template>