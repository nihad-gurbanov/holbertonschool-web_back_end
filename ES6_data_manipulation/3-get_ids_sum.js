function getStudentIdsSum (arr) {
  return arr.reduce((accumulator, currentObject) => accumulator + currentObject.id, 0);
}

export default getStudentIdsSum;